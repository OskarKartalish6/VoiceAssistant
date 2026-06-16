import ast
import operator as op
import re
from words2numsrus import NumberExtractor

from app.skills.base import Skill


SAFE_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)

    if isinstance(node, ast.BinOp):
        return SAFE_OPERATORS[type(node.op)](
            safe_eval(node.left),
            safe_eval(node.right)
        )

    if isinstance(node, ast.Constant):
        return node.value

    raise ValueError("Unsupported")


def normalize(text: str) -> str:

    text = text.replace("сколько будет", "")
    text = text.replace("плюс", "+")
    text = text.replace("минус", "-")
    text = text.replace("умножить на", "*")
    text = text.replace("разделить на", "/")
    text = text.replace("поделить на", "/")
    text = text.replace("степень", "**")

    return text


def extract_expression(text: str) -> str:
    text = normalize(text)
    extractor = NumberExtractor()
    text = extractor.replace_groups(text)
    match = re.findall(r"[0-9+\-*/(). ]+", text)
    print("".join(match).strip())
    return "".join(match).strip()


class CalculatorSkill(Skill):

    def can_handle(self, text: str) -> bool:
        phrases = ("сколько будет", "плюс",
                   "минус", "умножить", "разделить",
                   "степень")
        return any(phrase in text for phrase in phrases)

    def handle(self, text: str) -> str:
        expr = extract_expression(text)

        if not expr:
            return "Не понял выражение"

        try:
            node = ast.parse(expr, mode="eval")
            result = safe_eval(node)
            return f"Будет: {result}"

        except:
            return "Ошибка в вычислении"
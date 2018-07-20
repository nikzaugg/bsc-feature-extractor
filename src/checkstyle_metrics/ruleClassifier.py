from .categories import *

def classifyRule(inRule):
    rule = inRule.replace(" ", "")
    if rule in BEST_PRACTICE:
        return "BEST_PRACTICE"
    if rule in CODE_STRUCTURE:
        return "CODE_STRUCTURE"
    if rule in CONCURRENCY:
        return "CONCURRENCY"
    if rule in DOCUMENTATION_CONVENTIONS:
        return "DOCUMENTATION_CONVENTIONS"
    if rule in ERROR_HANDLING:
        return "ERROR_HANDLING"
    if rule in INTERFACE:
        return "INTERFACE"
    if rule in LOGIC:
        return "LOGIC"
    if rule in METRIC:
        return "METRIC"
    if rule in MIGRATION:
        return "MIGRATION"
    if rule in NAMING_CONVENTIONS:
        return "NAMING_CONVENTIONS"
    if rule in OBJECT_ORIENTED_DESING:
        return "OBJECT_ORIENTED_DESING"
    if rule in REFACTORINGS_REDUNDANCIES:
        return "REFACTORINGS_REDUNDANCIES"
    if rule in REFACTORINGS_SIMPLIFICATIONS:
        return "REFACTORINGS_SIMPLIFICATIONS"
    if rule in REGULAR_EXPRESSIONS:
        return "REGULAR_EXPRESSIONS"
    if rule in STYLE_CONVENTIONS:
        return "STYLE_CONVENTIONS"
    if rule in TOOL_SPECIFIC:
        return "TOOL_SPECIFIC"

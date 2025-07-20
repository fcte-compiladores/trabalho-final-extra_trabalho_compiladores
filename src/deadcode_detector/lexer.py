"""
Analisador Léxico - Tokenização do código Python
"""

import ast
from typing import List, Tuple, Any
from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    LITERAL = auto()
    OPERATOR = auto()
    DELIMITER = auto()
    COMMENT = auto()
    WHITESPACE = auto()
    NEWLINE = auto()


@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    node: Any = None


class Lexer:
    
    def __init__(self):
        self.tokens: List[Token] = []
        
    def tokenize(self, source_code: str) -> List[Token]:
        self.tokens = []
        
        try:
            tree = ast.parse(source_code)
            self._extract_tokens(tree, source_code)
            
        except SyntaxError as e:
            print(f"Erro de sintaxe na linha {e.lineno}: {e.text}")
            
        return self.tokens
    
    def _extract_tokens(self, tree: ast.AST, source_code: str):
        for node in ast.walk(tree):
            if hasattr(node, 'lineno') and hasattr(node, 'col_offset'):
                token_type = self._get_token_type(node)
                token_value = self._get_token_value(node, source_code)
                
                if token_value:
                    token = Token(
                        type=token_type,
                        value=token_value,
                        line=getattr(node, 'lineno', 0),
                        column=getattr(node, 'col_offset', 0),
                        node=node
                    )
                    self.tokens.append(token)
    
    def _get_token_type(self, node: ast.AST) -> TokenType:
        if isinstance(node, ast.Name):
            return TokenType.IDENTIFIER
        elif isinstance(node, (ast.Constant, ast.Num, ast.Str)):
            return TokenType.LITERAL
        elif isinstance(node, ast.keyword):
            return TokenType.KEYWORD
        elif isinstance(node, ast.operator):
            return TokenType.OPERATOR
        else:
            return TokenType.IDENTIFIER
    
    def _get_token_value(self, node: ast.AST, source_code: str) -> str:
        if hasattr(node, 'id'):
            return node.id
        elif hasattr(node, 'value'):
            return str(node.value)
        elif hasattr(node, 'arg'):
            return node.arg
        elif hasattr(node, 'attr'):
            return node.attr
        else:
            return str(node.__class__.__name__)
    
    def get_keywords(self) -> List[str]:
        return [token.value for token in self.tokens if token.type == TokenType.KEYWORD]
    
    def get_identifiers(self) -> List[str]:
        return [token.value for token in self.tokens if token.type == TokenType.IDENTIFIER] 
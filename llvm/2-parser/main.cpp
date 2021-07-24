#include "ast.cpp"
#include "parser.cpp"

int main() {
  auto LHS = std::make_unique<VariableExprAST>("x");
  auto RHS = std::make_unique<VariableExprAST>("y");
  auto Result =
      std::make_unique<BinaryExprAST>('+', std::move(LHS), std::move(RHS));
}
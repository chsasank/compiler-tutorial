#include "lexer.cpp"


int main()
{
  int tok = gettok();
  while (tok != tok_eof){
    tok = gettok();
    std::cout << " token " << tok << ", " << IdentifierStr << ", " << NumVal << std::endl; 
  }
  return 0;
}
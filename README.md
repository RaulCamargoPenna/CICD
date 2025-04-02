# CICD - Implantação de uma pipeline automatizada.

# Descrição:
Esse é um projeto que visa criar uma pipeline automatizada para projetos Django. Os workflows irão rodar a build e criar a PR automaticamente. Para evitar erros não faça pushs diretamente na main e sim utilizando a sua própria branch.


# Caso não tenha branch:
- Crie sua branch usando: git checkou -b MinhaBranch;
- Depois faça um commit: git commit -m 'Mensagem';
- Depois de um push usando --set-upstream para sinalizar ao git que os comando futuros devem se manter nessa branch: git push --set-upstream origin MinhaBranch;

Depois de ter feito essa configuração e criado sua branch você pode seguir com o desenvolvimento normalmente.

# Já tenho minha Branch:
- Ao abrir o terminal no local correto verifique em qual branch você está utilizando: git branch;
- Caso esteja na sua branch siga normalmente, caso contrário troque de branch utilizando: git switch MinhaBranch;
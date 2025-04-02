# **CICD - Implantação de uma Pipeline Automatizada**

## 📌 **Descrição**  
Este projeto tem como objetivo criar uma pipeline automatizada para projetos Django. Os workflows realizam a build e criam Pull Requests (PRs) automaticamente.  

⚠️ **Importante:** Não faça push diretamente na branch `main`. Sempre utilize sua própria branch para evitar conflitos e garantir um fluxo seguro de desenvolvimento.

---

## 🚀 **Como contribuir corretamente?**  

### 🔹 **Se ainda não tem uma branch**  
1. Crie uma nova branch:  
    ```sh
    git checkout -b MinhaBranch

2. Faça um commit das suas alterações:
    ```sh
    git commit -m 'Mensagem de commit'

3. Faça o primeiro push definindo a branch remota:
    ```sh
    git push --set-upstream origin MinhaBranch

### 🔹 **Se já tem uma branch**  
1. Abra o terminal e verifique se está na branch correta:
    ```sh
    git branch

2. Se estiver na sua branch, continue normalmente;
3. Caso precise trocar de branch, use:
    ```sh
    git switch MinhaBranch


### 🔎 **Por que estou usando arquivos separados?** 
> Como este é meu primeiro projeto de pipeline automatizada, optei por separar os workflows para facilitar a manutenção e escalabilidade.
> Além disso, a pipeline será integrada com diferentes ambientes (Homologação e Produção).
> Com essa abordagem, posso reutilizar o workflow Django CI nos scripts de Continuous Deployment (CD) para cada ambiente, utilizando workflow_run.
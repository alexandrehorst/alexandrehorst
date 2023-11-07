<h1 align="center">:file_cabinet: Baixador Automático de Imagens/ Automatic Photo Downloader README.md</h1>

## :memo: Descrição/ Description
Em decorrência de uma necessidade fazer download das fotos escolares dos meus filhos escrevi esse código.
A plataforma onde ficam hospedadas as fotos só permite o download de uma foto por vez, mas fazer o download de centenas de fotos uma a uma demoraria algumas horas. Além disso, como a plataforma é atualizada constatemente o processo necessitaria ser repetido diversas vezes.
Então criei uma automação usando Selenium que faz no login na plataforma, acessa a estrutura html da plataforma e busca as tags que contenham os links para download de cada foto (BeautifulSoup). Obtido os links, o programa salva as fotos.

I had a need: download my children's school photos. So, I wrote this code. 
The platform where the photos are hosted only allows you to download one photo at a time. Therefore to download hundreds of photos, it would  take time. Furthermore, the platform is constantly updated and I would need to be repeated the process several times. So I created an automation using Selenium that logs into the platform, accesses the platform's HTML code and searches for the tags that contain the download links for each photo (BeautifulSoup). Once the links are obtained, the program saves the photos.

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Jupyter Notebook versão 6.5.4 e o Python versão 3.11.4. Além disso, o código possui as seguintes dependências: 
* selenium==4.13.0;
* webdriver (ChromeDriver==116.0.5845.96);
* bs4==0.0.1; e
* O código depende também de um arquivo .py auxiliar contendo as credenciais do usuário para acesso ao site.

O arquivo do `webdriver.exe` deve ser colocado em um diretório que esteja no PATH do sistema operacional. Isso permitirá que o Python encontre o arquivo corretamente ao executar o código. Você pode colocar o `webdriver.exe` em um diretório como `C:\Windows` ou adicionar o diretório onde o arquivo está localizado ao PATH do sistema. Dessa forma, o Python conseguirá encontrá-lo durante a execução do código.

This code was developed using Jupyter Notebook version 6.5.4 and Python version 3.11.4. Additionally, the code has the following dependencies: 
* selenium==4.13.0;
* webdriver (ChromeDriver==116.0.5845.96);
* bs4==0.0.1; and
* The code also depends on an auxiliary file (credentials.py) containing the user's credentials to access the website.

The `webdriver.exe` file must be placed in a directory that is in the operating system's PATH. This will allow Python to find the file correctly when executing the code. You can place `webdriver.exe` in a directory like `C:\Windows` or add the directory where the file is located to the system PATH. This way, Python will be able to find it while executing the code.

## :books: Funcionalidades/ Features
* Realiza o download automático de todas as fotos que se encontram no site.
* Automatically downloads all photos found on the website.
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python;
* Webscraping;
* Web browser automation.

## :rocket: Rodando o projeto/ Running the code
Para rodar o código, o usuário precisa ter login e senha no site, os quais não serão disponibilizados aqui por questões de sigilo. Além disso, é necessário ter o webdriver correspondente ao browser utilizado (vide seção dependências).

Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.11.4
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.11.4)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando os comandos: pip install selenium==4.13.0 bs4==0.0.1
6) Executar o código: python "baixador_fotos.py"

To run the code, the user needs to have a login and password on the website, which will not be provided here for confidentiality reasons. Additionally, it is necessary to have the webdriver corresponding to the browser being used (see the dependencies section).

To run the code, follow these steps (using the Anaconda prompt):

1) Create a virtual environment in a specific directory: conda create -n <venv_name> python=3.11.4
2) Activate the virtual environment: conda activate <venv_name>
3) Verify if everything is okay: python --version (you should see the message: Python 3.11.4)
4) Using the prompt, navigate to the directory where the code files are located.
5) Install the dependencies using the following commands: pip install selenium==4.13.0 bs4==0.0.1
6) Execute the code: python "baixador_fotos.py"

## :dart: Status do projeto/ Project Status
O projeto está finalizado.

The project is done.

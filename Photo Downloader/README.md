<h1 align="center">:file_cabinet: Photo Downloader README.md</h1>

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
* urllib.request==3.11;
* bs4==4.12.2; e
* O código depende também de um arquivo .py auxiliar contendo as credenciais do usuário para acesso ao site.

O arquivo do `webdriver.exe` deve ser colocado em um diretório que esteja no PATH do sistema operacional. Isso permitirá que o Python encontre o arquivo corretamente ao executar o código. Você pode colocar o `webdriver.exe` em um diretório como `C:\Windows` ou adicionar o diretório onde o arquivo está localizado ao PATH do sistema. Dessa forma, o Python conseguirá encontrá-lo durante a execução do código.

This code was developed using Jupyter Notebook version 6.5.4 and Python version 3.11.4. Additionally, the code has the following dependencies: 
* selenium==4.13.0;
* webdriver (ChromeDriver==116.0.5845.96);
* urllib.request==3.11; and
* bs4==4.12.2; and
* The code also depends on an auxiliary credentials.py file containing the user's credentials to access the website.

The `webdriver.exe` file must be placed in a directory that is in the operating system's PATH. This will allow Python to find the file correctly when executing the code. You can place `webdriver.exe` in a directory like `C:\Windows` or add the directory where the file is located to the system PATH. This way, Python will be able to find it while executing the code.

## :books: Funcionalidades/ Features
* Realiza o download automático de todas as fotos que se encontram no site.
* Automatically downloads all photos found on the website.
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Webscraping

## :rocket: Rodando o projeto/ Running the code
Para rodar o código, o usuário precisa ter login e senha no site, os quais não serão disponibilizados aqui.

To run the code, the user must have credentias to acess the website.

## :dart: Status do projeto/ Project Status
O projeto está finalizado.

The project is done.

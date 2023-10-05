Em decorrência de uma necessidade fazer download das fotos escolares dos meus filhos escrevi esse código.
A plataforma onde ficam hospedadas as fotos só permite o download de uma foto por vez, mas fazer o download de centenas de fotos uma a uma demoraria algumas horas. Além disso, como a plataforma é atualizada constatemente o processo necessitaria ser repetido diversas vezes.
Então criei uma automação usando Selenium que faz no login na plataforma, acessa a estrutura html da plataforma e busca as tags que contenham os links para download de cada foto (BeautifulSoup). Obtido os links, o programa salva as fotos.

Due to the need to download my children's school photos, I wrote this code. 
The platform where the photos are hosted only allows you to download one photo at a time, but you can download hundreds of photos one by one would take a few hours. Furthermore, as the platform is constantly updated, the process would need to be repeated several times.
So I created an automation using Selenium that logs into the platform, accesses the platform's HTML code and searches for the tags that contain the download links for each photo (BeautifulSoup). Once the links are obtained, the program saves the photos.

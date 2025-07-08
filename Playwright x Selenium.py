#✅ 1. Propósito
#Ambos: Automação de navegadores para testes e raspagem de dados.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
print(driver.title)
driver.quit()

#✅ Resumo do que faz:
#Abre o Google Chrome.
#Acessa o site https://example.com.
#Mostra o título da página.
#Fecha o navegador.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()

#✅ Resumo do que faz:
#Abre o navegador Chromium (parecido com o Chrome).
#Acessa o site https://example.com.
#Imprime o título da página.
#Fecha o navegador.

#✅ Notas Importantes:
#Ambos acessam um site e capturam o título, mas o Playwright é mais flexível para rodar em modo "headless" ou com múltiplas abas.
#No Playwright, você pode trocar p.chromium.launch() por p.chromium.launch(headless=False) para ver o navegador abrindo.
#No Selenium, a configuração headless também é possível, mas exige adicionar opções manualmente.
#✅ Resumo final:
#Os dois códigos fazem o mesmo: abrem o navegador, acessam um site e imprimem o título.
#O Playwright, porém, faz isso de forma mais moderna e segura, já criando o ambiente de execução automaticamente com with.

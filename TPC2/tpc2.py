import re

def markdown_to_html(markdown):
    #cabeçalho
    markdown = re.sub(r'^(#{1,6})\s(.+)$', r'<\1>\2</\1>', markdown, flags=re.MULTILINE)
    
    #Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    
    #Italico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    
    #Lista numerada
    markdown = re.sub(r'^(\d+)\.\s(.+)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    markdown = '<ol>\n' + markdown + '</ol>'
    
    #Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    
    #Image
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)' , r'<img src="\2" alt="\1"/>', markdown)
    
    return markdown
    
#Exemplo de teste
markdown = """
# Exemplo de cabeçalho
Este é um exemplo com formatação em Markdown

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [pagina da uc](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html = markdown_to_html(markdown)
print(html)
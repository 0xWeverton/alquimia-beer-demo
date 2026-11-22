# Alquimia Beer — demonstração de loja

Loja virtual estática (HTML, CSS e JavaScript) para apresentação ao Bryan, da Alquimia Beer, em Esteio-RS.

O catálogo, os preços e as imagens são de exemplo. O pedido é montado no navegador e enviado como texto formatado para o WhatsApp da loja, sem backend.

## Como abrir

Abra `index.html` em um servidor local (abrir o arquivo direto também funciona, mas um servidor é mais previsível):

```bash
python3 -m http.server 8080
```

## Ajuste rápido

No topo de `app.js`:

- `WHATSAPP_NUMBER` — número no formato internacional, sem `+`
- `TAXA_ENTREGA` — valor em reais
- `HORARIOS` — funcionamento no fuso `America/Sao_Paulo`

## Aviso

Demonstração – produtos e preços de exemplo.

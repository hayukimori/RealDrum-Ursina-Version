# RealDrum Ursina

### Descrição

RealDrum Ursina Version é uma versão alternativa do aplicativo RealDrum (android), mas focando em usuários de PC (Mais especificamente Linux).

![](demo_img.png)

### Requisitos e Execução do programa
Aqui estão os pacotes necessários para executar e como executar, assim como informações adicionais sobre o arquivo `drumconfig.py`

##### Pacotes necessários
Os seguintes pacotes são necessários para executar corretamente o programa:

```
python3 - pode ser encontrado por padrão na distro
ursina - instalado via pip (python3 -m pip install ursina)
```

##### Como executar
Para executar, basta executar o comando `python3 main.py` dentro da pasta do programa.

#### Arquivo "drumconfig"
Este arquivo contém as configurações da bateria virtual. Desde kit que será utilizado à volumes.

- `#Kit` - A variável `kit` guarda o nome do kit que será utilizado. Você pode trocar o valor para o nome de algum kit que tenha dentro da pasta `drumkits`

- `#Teclas` - É o mapeamento das teclas para interação com a bateria. Note que algumas não tem dois valores, não recomendo que adicione um valor a mais nelas

- `#Volume` - As variáveis dentro dessa seção guardam o volume/altura de cada nota.

## Adicional
Você pode adicionar mais kits e utilizá-los no RealDrumUrsina.
Para adicionar, basta pegar um arquivo de exportação de kit, que pode conseguir compartilhando direto do RealDrum (android), extrair o arquivo `.realdrum`, renomear a pasta que há dentro dele e mover para onde estão os outros drumkits.

Observação: O arquivo `.realdrum` pode ser extraído como um arquivo `.zip`

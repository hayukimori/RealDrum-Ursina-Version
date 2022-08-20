# RealDrum Ursina

### Descrição

RealDrum Ursina Version é uma versão alternativa do aplicativo RealDrum (android), mas focando em usuários de PC (Mais especificamente Linux).

![](demo_img.png)

### Requisitos e Execução do programa
Aqui estão os pacotes necessários para executar e como executar, assim como informações adicionais sobre o arquivo `config.ini`

##### Pacotes necessários
Os seguintes pacotes são necessários para executar corretamente o programa:

```
python3 - pode ser encontrado por padrão na distro
ursina - instalado via pip (python3 -m pip install ursina)
```

##### Como executar
Para executar, basta executar o comando `python3 main.py` dentro da pasta do programa.

#### Arquivo "config.ini"
Este arquivo contém as configurações da bateria virtual. Desde kit que será utilizado à volumes.

- `#general` - A variável `drumkit` guarda o nome do kit que será utilizado. Você pode trocar o valor para o nome de algum kit que tenha dentro da pasta `drumkits`

- `#keys` - É o mapeamento das teclas para interação com a bateria. A adição de mais uma tecla não fará efeito.

- `#volume` - Esta seção guarda os volumes de cada parte da bateria.

## Adicional
Você pode adicionar mais kits e utilizá-los no RealDrumUrsina.
Para adicionar, basta adiquirir um arquivo de exportação de kit, que pode conseguir compartilhando direto do RealDrum (android), extrair o arquivo `.realdrum`, renomear a pasta que há dentro dele e mover para onde estão os outros drumkits.

Observação: O arquivo `.realdrum` pode ser extraído assim como um arquivo `.zip`

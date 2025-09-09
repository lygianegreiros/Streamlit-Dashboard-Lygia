```markdown
# 🌾 Dashboard IoT - Umidade & Temperatura (ThingSpeak)

Este projeto é um **dashboard interativo** desenvolvido em **Python + Streamlit**, que consome dados de um canal público do [ThingSpeak](https://thingspeak.com/) e apresenta visualizações para **Umidade** e **Temperatura** em tempo real.

---

## 📌 Funcionalidades
- 📈 **Gráfico de linha**: evolução dos dados ao longo do tempo  
- 📊 **Gráfico de barras**: distribuição dos valores  
- 🥧 **Gráfico de pizza**: proporção por faixas de valores  
- 🔎 **Métricas principais**: último valor registrado, média, máximo e mínimo  

---

## 🛠️ Tecnologias utilizadas
- [Python 3.11+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Plotly](https://plotly.com/python/)  
- [ThingSpeak API](https://thingspeak.com/docs/)  

---

## 📂 Estrutura do projeto
```

📁 projeto-iot
┣ 📄 app.py       # Código principal do dashboard
┣ 📄 requirements.txt  # Dependências do projeto
┗ 📄 README.md    # Documentação

````

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/projeto-iot.git
cd projeto-iot
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Streamlit

```bash
streamlit run app.py
```

O app ficará disponível em: [http://localhost:8501](http://localhost:8501)

---

## 🔗 Fonte dos dados

* Canal público do **ThingSpeak**:
  [https://api.thingspeak.com/channels/2943258/feeds.json](https://api.thingspeak.com/channels/2943258/feeds.json)
* Campos:

  * `Umidade (%)`
  * `Temperatura (°C)`

---

## 📊 Exemplo de visualização

![Exemplo Dashboard](https://streamlit.io/images/brand/streamlit-mark-color.png)

---

## 🤝 Contribuição

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias e novas visualizações.

---

## 📜 Licença

Este projeto é de uso acadêmico e livre para estudos.

```

---

👉 Quer que eu também gere o **`requirements.txt`** com as libs corretas para você já colocar no repositório?
```

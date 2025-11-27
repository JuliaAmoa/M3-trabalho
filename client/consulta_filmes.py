"""Como usar
1. Certifique-se de que o servidor está rodando em http://localhost:8000
2. Execute: python client/query_movie.py
3. Digite o título do filme quando solicitado"""
import requests

def main():
    titulo = input("Digite o título do filme: ").strip()
    if not titulo:
        print("Título vazio.")
        return
    try:
        r = requests.get("http://localhost:8000/filme", params={"titulo": titulo}, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # Formata o dicionário de resposta para exibição no console.
            print("\nResultado:")
            print(f"Titulo : {data['titulo']}")
            print(f"Ano    : {data['ano']}")
            print(f"Sinopse: {data['sinopse']}\n")
        else:
            print(f"Erro {r.status_code}: {r.text}")
    except requests.exceptions.RequestException as e:
        print("Erro de rede ao conectar ao servidor:", e)

if __name__ == "__main__":
    main()
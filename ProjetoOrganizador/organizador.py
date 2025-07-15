import os
import shutil
import time

caminho_da_pasta = os.path.join(os.getcwd(), 'MINHA_BAGUNCA')


MAPA_DE_PASTAS = {
    '.pdf': 'Documentos PDF',
    '.docx': 'Documentos Word',
    '.xlsx': 'Planilhas Excel',
    '.pptx': 'Apresentações',
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.zip': 'Arquivos Compactados',
    '.rar': 'Arquivos Compactados',
    '.exe': 'Executáveis',
    '.mp3': 'Músicas',
    '.mp4': 'Vídeos',
    
}

#FUNÇÃO PRINCIPAL
def organizar_pasta(caminho):
    print(f"Iniciando organização da pasta: {caminho}\n")
    time.sleep(2) # Uma pequena pausa para o usuário ler a mensagem

    # Lista todos os arquivos 
    arquivos_na_pasta = os.listdir(caminho)

    for nome_arquivo in arquivos_na_pasta:
        # Pega o caminho completo do arquivo
        caminho_arquivo_completo = os.path.join(caminho, nome_arquivo)

        # Verifica se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_arquivo_completo):
            try:
                # Separa o nome do arquivo da sua extensão
                nome, extensao = os.path.splitext(nome_arquivo)
                extensao = extensao.lower() # Converte a extensão para minúscula

                # Se a extensão estiver no nosso mapa...
                if extensao in MAPA_DE_PASTAS:
                    # Pega o nome da pasta de destino do mapa
                    pasta_destino = MAPA_DE_PASTAS[extensao]
                    caminho_pasta_destino = os.path.join(caminho, pasta_destino)

                    # Cria a pasta de destino se ela não existir
                    if not os.path.exists(caminho_pasta_destino):
                        os.makedirs(caminho_pasta_destino)
                        print(f"[CRIANDO PASTA]: {pasta_destino}")

                    # Move o arquivo para a pasta de destino
                    shutil.move(caminho_arquivo_completo, caminho_pasta_destino)
                    print(f"✔️ Movido '{nome_arquivo}' para '{pasta_destino}'")

                # Se não, podemos ignorar ou mover para uma pasta 'Outros'
                else:
                    print(f"❓ Arquivo '{nome_arquivo}' não tem uma categoria definida. Ignorando.")

            except Exception as e:
                print(f"❌ Erro ao processar o arquivo '{nome_arquivo}': {e}")
    
    print("\nOrganização concluída!")

# 4. EXECUTANDO A FUNÇÃO
if __name__ == "__main__":
    organizar_pasta(caminho_da_pasta)
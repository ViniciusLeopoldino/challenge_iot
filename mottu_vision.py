import cv2
from pyzbar.pyzbar import decode
import numpy as np
import json

def ler_qr_da_camera():
    cap = cv2.VideoCapture(0)
    print("Aguardando leitura do QR Code... Pressione 'Ctrl + C' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar e decodificar QR Codes na imagem
        for barcode in decode(frame):
            pontos = np.array([barcode.polygon], np.int32)
            pontos = pontos.reshape((-1, 1, 2))
            cv2.polylines(frame, [pontos], True, (0, 255, 0), 3)

            qr_data = barcode.data.decode('utf-8')
            try:
                dados = json.loads(qr_data)
                texto = f"{dados.get('placa')} - {dados.get('modelo')}"
            except:
                dados = {}
                texto = qr_data

            x, y, w, h = barcode.rect
            cv2.putText(frame, texto, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            print("✅ QR Code Detectado:")
            print(dados)
            print("Simulando armazenamento: Armazém A1-R1-M1-C1\n")

        cv2.imshow("Mottu Vision - Leitor QR", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ler_qr_da_camera()

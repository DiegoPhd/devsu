 ## Requisitos Previos

1. Clonar el presente repositorio
2. Abrir el repositorio en el IDE de preferencia (Recomiendo VSCode) en la carpeta `DEVSU`
4. Crear y activar un entorno virtual:
    ```
    python -m venv env
    env\Scripts\Actvivate.ps1
    ```
5. Instalar dependencias
    ```
    pip install -r config/requirements.txt
    ```
6. Instalar [Allure Report](https://allurereport.org/docs/install/)

## Ejecución pruebas E2E back y front

- Para ejecutar los tests:
    ```
    allure generate --clean --output allure_report; pytest --alluredir allure_report/
    ```
- Para construir el reporte:
    ```
    allure generate -c allure_report/ -o report; allure-combine report
    ```
- Para visualizar el reporte hay dos opciones:
    - Abrir el archivo `report/complete.html` en el navegador de preferencia
    - Generar servidor con el reporte `allure serve allure_report`

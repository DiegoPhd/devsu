 # Requisitos Previos

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

# Ejecución pruebas E2E Frontend

- Para ejecutar los tests `allure generate --clean --output allure_report; pytest -v saucedemo/tests --alluredir allure_report/`
- Para visualizar el reporte: `allure serve allure_report`

# Ejecución E2E Backend
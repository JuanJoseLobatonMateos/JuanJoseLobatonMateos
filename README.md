# ¡Hola, soy Juan José Lobatón Mateos! 👋

Bienvenido a mi perfil de GitHub. Aquí encontrarás información sobre mis proyectos, intereses y cómo contactarme.

<div align="center">
  <img src="https://avatars.githubusercontent.com/u/your-username" width="150" height="150" alt="Juan José Lobatón Mateos">
  <h2>Juan José Lobatón Mateos</h2>
  <p>Desarrollador apasionado por la tecnología y la programación.</p>
</div>

## 📝 Sobre mí

Soy un desarrollador con experiencia en diversas áreas, incluyendo desarrollo web, análisis de datos y automatización de procesos. Me encanta aprender nuevas tecnologías y compartir mis conocimientos con la comunidad.

A los 40 años, decidí dar un giro en mi vida laboral y dedicarme a lo que realmente me apasiona: la programación. Actualmente, soy estudiante de CFGS de Desarrollo de Aplicaciones Multiplataforma, lo que me ha permitido adquirir habilidades y conocimientos en diferentes tecnologías y herramientas.

## 🚀 Proyectos Destacados

Aquí tienes algunos de mis proyectos más destacados:

- [**Nombre del Proyecto 1**](https://github.com/JuanJoseLobatonMateos/proyecto1): Breve descripción del proyecto y su propósito.
- [**Nombre del Proyecto 2**](https://github.com/JuanJoseLobatonMateos/proyecto2): Breve descripción del proyecto y su propósito.
- [**Nombre del Proyecto 3**](https://github.com/JuanJoseLobatonMateos/proyecto3): Breve descripción del proyecto y su propósito.

## 🛠️ Tecnologías y Herramientas

Aquí están algunas de las tecnologías y herramientas con las que trabajo:

<div align="center">
  <img src="https://img.shields.io/badge/-Java-007396?style=for-the-badge&logo=java&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/-Android_Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white" alt="Android Studio">
  <img src="https://img.shields.io/badge/-Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin">
  <img src="https://img.shields.io/badge/-NetBeans-1B6AC6?style=for-the-badge&logo=apachenetbeanside&logoColor=white" alt="NetBeans">
  <img src="https://img.shields.io/badge/-Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white" alt="Eclipse">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/-Hibernate-59666C?style=for-the-badge&logo=hibernate&logoColor=white" alt="Hibernate">
  <img src="https://img.shields.io/badge/-XML-FF6600?style=for-the-badge&logo=xml&logoColor=white" alt="XML">
  <img src="https://img.shields.io/badge/-HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/-CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/-JUnit-25A162?style=for-the-badge&logo=junit5&logoColor=white" alt="JUnit">
  <img src="https://img.shields.io/badge/-iReports-4B8BBE?style=for-the-badge&logo=ireports&logoColor=white" alt="iReports">
</div>

## 🚀 GitHub Actions

Utilizo GitHub Actions para automatizar flujos de trabajo de desarrollo, incluyendo integración continua (CI) y entrega continua (CD). Aquí hay algunos ejemplos de cómo uso GitHub Actions en mis proyectos:

- **Automatización de pruebas**: Cada vez que hago un push a la rama principal, se ejecutan pruebas automatizadas para asegurar que el código sea estable.
- **Despliegue automático**: Después de pasar todas las pruebas, el código se despliega automáticamente a un entorno de producción.
- **Análisis de código**: Ejecuto análisis de código estático para mantener la calidad del código y detectar posibles errores.

Aquí tienes un ejemplo básico de un workflow de GitHub Actions que ejecuta pruebas en una aplicación Java:

```yaml
name: Java CI

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up JDK 11
      uses: actions/setup-java@v2
      with:
        java-version: '11'

    - name: Build with Gradle
      run: ./gradlew build

    - name: Run tests
      run: ./gradlew test

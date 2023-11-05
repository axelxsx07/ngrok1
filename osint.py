import requests

def search_on_facebook(username):
    # Aquí puedes implementar la búsqueda en Facebook si tienes acceso a su API.
    # Facebook no proporciona búsqueda pública sin autenticación.

    # Para acceder a la API de Facebook, necesitarás obtener un token de acceso válido
    # y seguir sus políticas de uso. Esto puede ser más complejo que otros servicios.

    return None

def search_on_tiktok(username):
    url = f'https://www.tiktok.com/@{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return f'TikTok: {url}'
    return None

def search_on_twitter(username):
    url = f'https://twitter.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return f'Twitter: {url}'
    return None

def search_on_instagram(username):
    url = f'https://www.instagram.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return f'Instagram: {url}'
    return None

def search_on_github(username):
    url = f'https://github.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return f'GitHub: {url}'
    return None

def main():
    username = input("Ingresa el nombre de usuario a verificar: ")

    results = []

    tiktok_result = search_on_tiktok(username)
    if tiktok_result:
        results.append(tiktok_result)

    twitter_result = search_on_twitter(username)
    if twitter_result:
        results.append(twitter_result)

    instagram_result = search_on_instagram(username)
    if instagram_result:
        results.append(instagram_result)

    github_result = search_on_github(username)
    if github_result:
        results.append(github_result)

    facebook_result = search_on_facebook(username)
    if facebook_result:
        results.append(facebook_result)

    if results:
        print(f"Se encontraron coincidencias para '{username}':")
        for result in results:
            print(result)
    else:
        print(f"No se encontraron coincidencias para '{username}' en las redes sociales verificadas.")

if __name__ == "__main__":
    main()

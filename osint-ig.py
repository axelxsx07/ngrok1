import instaloader

def obtener_informacion_perfil(username):
    L = instaloader.Instaloader()
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print("Username:", profile.username)
        print("Nombre completo:", profile.full_name)
        print("Biografía:", profile.biography)
        print("Seguidores:", profile.followers)
        print("Siguiendo:", profile.followees)
        print("Publicaciones:", profile.mediacount)

        for post in profile.get_posts():
            print("URL de la publicación:", post.url)
            print("Descripción de la publicación:", post.caption)
            print("Likes:", post.likes)
            print("Comentarios:", post.comments)
            print("Fecha de publicación:", post.date)

    except instaloader.exceptions.ProfileNotExistsException:
        print("El perfil no existe.")

if __name__ == "__main__":
    username = "soy.axelxs"  # Reemplaza con el nombre de usuario que desees investigar
    obtener_informacion_perfil(username)


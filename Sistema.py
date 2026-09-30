from Usuario import Estudiante, Docente

if __name__ == "__main__":
    print("====================================================")
    print("[SISTEMA] Registrando usuarios...")
    alumno = Estudiante(
        id_usuario="IS_III_SR- 4", 
        nombre="Ivan Bejarano", 
        email="isbejarano_usistemas@intep.edu.co", 
        carrera="Ingeniería de Sistemas"
    )
    
    profesor = Docente(
        id_usuario="DOC_IS-01", 
        nombre="Hermes Vladimir", 
        email=""
    )
    
    print(alumno.ver_perfil())
    print(profesor.ver_perfil())
    print("====================================================")

    print("\n[ACCIONES DOCENTE]")
    materia_objetivo = "Programación Orientada a Objetos"
    
    profesor.crear_chat_relacionado(materia_objetivo)
    
    profesor.administrar_materia(materia_objetivo)
    chat_academico = profesor.crear_chat_relacionado(materia_objetivo)
    
    print("\n[Opciones para estudiante]")
    alumno.inscribir_materia(materia_objetivo)
    
    if chat_academico:
        alumno.unirse_a_chat(chat_academico)
        
    print("\n====================================================")
    print("tarea numero 2 finalizada con éxito")

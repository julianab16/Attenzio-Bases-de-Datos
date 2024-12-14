import { StyleSheet } from "react-native";
const { width, height } = Dimensions.get("window");

export const productstyle = StyleSheet.create({
    container: { 
        flex: 1, 
        backgroundColor: '#fff', 
        
    }, 
    text: { 
        fontSize: 20, 
        color: '#000', 
    },
    imagenPerfile:{
        borderRadius: 0,
        borderColor: "white",
        width: width * 0.9,
        height: height * 775,
        resizeMode: "contain",
    },
    topBar: {
        height: 50, // Altura de la barra amarilla
        backgroundColor: "#f4ce6a", // Color amarillo
      },
      content: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        paddingHorizontal: 20,
      },
      logo: {
        width: width * 0.4, // Tamaño proporcional para el logo del niño
        height: width * 0.4,
        resizeMode: "contain",
        marginBottom: 20,
      },
      textImage: {
        width: width * 0.6, // Tamaño proporcional para el texto "Attenzio"
        height: width * 0.2,
        resizeMode: "contain",
        marginBottom: 40,
      },
      button: {
        backgroundColor: "#f4ce6a", // Color amarillo
        paddingVertical: 15,
        paddingHorizontal: 50,
        borderRadius: 10,
        marginBottom: 20,
      },
      buttonText: {
        color: "#000", // Texto negro
        fontSize: 18,
        fontWeight: "bold",
      },
      signUpText: {
        fontSize: 14,
        color: "#000",
      },
      signUpLink: {
        color: "#f4ce6a", // Amarillo para el link
        fontWeight: "bold",
      },
});
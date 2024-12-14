import { StyleSheet } from "react-native";
const { width, height } = Dimensions.get("window");


export const productstyle = StyleSheet.create({
    container: { 
        flex: 1, 
        backgroundColor: '#fff', 
        alignItems: 'center', 
        justifyContent: 'center', 
    }, 
    text: { 
        fontSize: 20, 
        color: '#000', 
    },
    imagenPerfile:{
        borderRadius: 0,
        borderColor: "white",
        width: width * 0.9,
        height: height * 0.7,
        resizeMode: "contain",
    },
});
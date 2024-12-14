import React from 'react';
import { Text, View, SafeAreaView, StatusBar, Image} from 'react-native';
import {productstyle} from '../styles/InicioStyles';

export default function Inicio() {
    return(
        <SafeAreaView style={productstyle.container}>
      {/* Barra superior */}
      <View style={styles.topBar} />

      {/* Contenido central */}
      <View style={productstyle.content}>
        {/* Logotipo (niño leyendo) */}
        <Image style={productstyle.logo} source={require("../assets/logo.png")} />
       
        {/* Texto Attenzio */}
        <Image style={productstyle.textImage} source={require("../assets/Attenzio.png")}/>
        
        {/* Botón Login */}
        <TouchableOpacity style={productstyle.button}>
          <Text style={productstyle.buttonText}>Login</Text>
        </TouchableOpacity>
        
        {/* Texto Sign up */}
        <Text style={productstyle.signUpText}>
          Don't have an account?{" "}
          <Text style={productstyle.signUpLink} onPress={() => navigation.navigate("SignUp")}>
            Sign up
          </Text>
        </Text>
      </View>
    </SafeAreaView>
    );
}
import React from 'react';
import { Text, View, SafeAreaView, StatusBar, Image} from 'react-native';
import {productstyle} from '../styles/InicioStyle';

export default function Inicio() {
    return(
        <SafeAreaView style={productstyle.container}> 
        <StatusBar barStyle="dark-content" /> 
        <View style={productstyle.c}>
            <Image style={productstyle.imagenPerfile} source={require('../assets/Attenzio.png')} />
        </View>
        </SafeAreaView>
    );
}
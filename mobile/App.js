import { StatusBar } from 'expo-status-bar';
import "react-native-gesture-handler";
import { createStackNavigator} from "@react-navigation/stack";
import Inicio from "./screens/Inicio";
import { NavigationContainer } from "@react-navigation/native";


export default function App() {
  const Stack= createStackNavigator();
  function MyStack(){
    return(
      <Stack.Navigator screenOptions={{headerShown:false}}>
        <Stack.Screen name="Inicio" component={Inicio}/>

      </Stack.Navigator>

    );
  }
  return(
    <NavigationContainer>
      <MyStack/>
    </NavigationContainer>
  );
}


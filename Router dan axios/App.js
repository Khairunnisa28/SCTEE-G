import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import User from "./pages/User";
import Data from "./pages/cek_data";

function App(){
  return(
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/player' element={<User/>}/>
      <Route path='/data' element={<Data/>}/>
    </Routes>
  )
}

export default App;
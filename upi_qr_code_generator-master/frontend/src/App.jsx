import { UserInput } from "./components/UserInput/UserInput";
import { QRImage } from "./components/UserInput/QRImage";
import React from "react";
import { ImageContext } from "./storage/app-context";

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

function App() {
  return (
<ImageContext.Provider value= {{img:'https://dummyimage.com/160x160/fff/aaa&text=QR+Code'}}>
  <UserInput/>
</ImageContext.Provider>

  );
}

export default App;

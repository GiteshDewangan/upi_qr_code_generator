import React from "react";
import { useState, useContext } from "react";

export const ImageContext = React.createContext({img:''});

// const ImageContext = React.createContext();
// const ImageUpdateContext = React.createContext();

// export function useImage(){
//     return useContext(ImageContext)
// }
// export function useImageUpdate(){
//     return useContext(ImageUpdateContext)
// }
// export function ImageProvider({ children }) {
//   const [imgData, setImgData] = useState("");
//   function updateImage(data) {
//     setImgData(data);
//   }
//   return (
//     <ImageContext.Provider value={imgData}>
//       <ImageUpdateContext.Provider
//         value={(data) => {
//           updateImage(data);
//         }}
//       >
//         {children}
//       </ImageUpdateContext.Provider>
//     </ImageContext.Provider>
//   );
// }

import { useEffect, useState } from "react"
import { useContext } from "react"
import { ImageContext } from "../../storage/app-context";
export function QRImage() {
const imgData = useContext(ImageContext)

return(
  <div>
    <h3>QR Code</h3>
  <img  src={imgData.img} />

  </div>
)
}
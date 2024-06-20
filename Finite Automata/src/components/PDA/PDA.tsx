import Forms from "../Forms/Forms";
import Header from "../Header/Header";
import { useState, useEffect } from "react";
import "./pda.css";
import Form from "react-bootstrap/Form";
import Template1Form from "../Forms/Template1Form";
import Template2Form from "../Forms/Template2Form";
import {SITE} from "../../constants.ts";

const PDA = () => {
  const [result, setResult] = useState(false);
  const [showCustom, setShowCustom] = useState(true);
  const [showTemplate1, setShowTemplate1] = useState(false);
  const [showTemplate2, setShowTemplate2] = useState(false);

  useEffect(() => {
    const iframe = document.getElementById("hiddenframe");
    console.log("Asdjasd");

    if (iframe) {
      iframe.addEventListener("load", async () => {
        const res = await fetch(SITE + "PDA");
        const data = await res.json();

        console.log(res);
        console.log(data);
        console.log(data.valid);
        setResult(data.valid);
      });
    } else {
      console.log("no");
    }
  }, [showCustom, showTemplate1, showTemplate2]);
  return (
    <>
      <Header />
      <h1>PUSHDOWN AUTOMATA</h1>
      {result ? <h2 style={{
          backgroundColor: "forestgreen",
          padding: 10
      }}>String is valid</h2> :
          <h2 style={{
              backgroundColor: "orangered",
              padding: 10
          }}>String is invalid</h2>}
      <br></br>

      <Form.Select
        onChange={(e) => {
          setShowCustom(e.target.value === "Create your own PDA");
          setShowTemplate1(
            e.target.value === "PDA that accepts equal 0s and 1s (0s must precede 1s)"
          );
          setShowTemplate2(
            e.target.value === "PDA that accepts twice the 1s than 0s (0s must precede 1s)"
          );
        }}
      >
        <option>Create your own PDA</option>
        <option>PDA that accepts equal 0s and 1s (0s must precede 1s)</option>
        <option>PDA that accepts twice the 1s than 0s (0s must precede 1s)</option>
      </Form.Select>
      {showCustom && <Forms />}
      {showTemplate1 && <Template1Form />}
      {showTemplate2 && <Template2Form />}
    </>
  );
};

export default PDA;

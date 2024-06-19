import { useState } from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import TransitionFunctionForm from "./TransitionFunctionForm";
import { Button } from "react-bootstrap";
import StateForm from "./StateForm";

const Forms = () => {
  const [validated, setValidated] = useState(false);
  const [stateCounter, setStateCounter] = useState(1);
  const SITE = "https://finite-automata-checker.onrender.com/";

  const handleSubmit = (event: any) => {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      console.log("invalid");
      event.preventDefault();
      event.stopPropagation();
      return;
    }
    console.log("submit");

    setValidated(true);
  };

  const handleAddStateClick = () => {
    setStateCounter(stateCounter + 1);
  };
  const handleDeleteStateClick = () => {
    if (stateCounter === 0) {
      return;
    }
    setStateCounter(stateCounter - 1);
  };

  return (
    <>
      <Form
        noValidate
        validated={validated}
        action={SITE + "PDA"}
        method="POST"
        target="hiddenframe"
        onSubmit={handleSubmit}
      >
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">Input String</InputGroup.Text>
          <Form.Control
            required
            id="inputString"
            name="InputString"
            placeholder="Input String"
            aria-label="Input String"
            aria-describedby="basic-addon1"
          />
        </InputGroup>
        <button type="button" onClick={handleAddStateClick}>
          Add State
        </button>
        <button type="button" onClick={handleDeleteStateClick}>
          Delete State
        </button>
        <StateForm stateCount={stateCounter} />
        <TransitionFunctionForm stateCount={stateCounter} />
        <Button type="submit">Test String</Button>
      </Form>
      <iframe id="hiddenframe" name="hiddenframe"></iframe>
    </>
  );
};

export default Forms;

import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import TransitionFunctionForm from "./TransitionFunctionForm";
import { Button } from "react-bootstrap";
import StateForm from "./StateForm";

const Forms = () => {
  const [validated, setValidated] = useState(false);

  const handleSubmit = (event: any) => {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
    }

    setValidated(true);
  };

  return (
    <>
      <Form
        noValidate
        validated={validated}
        action="http://127.0.0.1:5000/PDA"
        method="POST"
        onSubmit={handleSubmit}
      >
        <Form.Label>Input String</Form.Label>
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
          <Form.Control
            required
            name="InputString"
            placeholder="Input String"
            aria-label="Input String"
            aria-describedby="basic-addon1"
          />
        </InputGroup>
        <StateForm />
        <TransitionFunctionForm />
        <Button type="submit">Test String</Button>
      </Form>
    </>
  );
};

export default Forms;

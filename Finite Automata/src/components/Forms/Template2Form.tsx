import { useState } from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import { Button } from "react-bootstrap";
import TransitionFunctionTemplateForm from "./TransitionFunctionTemplateForm";
import StateTemplateForm from "./StateTemplateForm";

const Template1Form = () => {
  const [validated, setValidated] = useState(false);
  const SITE = "https://finite-automata-checker.onrender.com/";

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
        action={SITE + "PDA"}
        method="POST"
        target="hiddenframe"
        onSubmit={handleSubmit}
      >
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">Input String</InputGroup.Text>
          <Form.Control
            required
            name="InputString"
            placeholder="Input String"
            aria-label="Input String"
            aria-describedby="basic-addon1"
          />
        </InputGroup>

        <Form.Label>States</Form.Label>

        {/* <StateForm stateCount={stateCounter} /> */}
        <Form.Group>
          <StateTemplateForm index={0} finalState={"off"} />
          <StateTemplateForm index={1} finalState={"off"} />
          <StateTemplateForm index={2} finalState={"on"} />
        </Form.Group>

        <Form.Label>Transition Functions</Form.Label>
        {/* <TransitionFunctionForm stateCount={stateCounter} /> */}
        <Form.Group>
          <TransitionFunctionTemplateForm
            ruleNumber={0}
            currentState={"q0"}
            inputSymbol={"0"}
            stackTop={"Z"}
            nextState={"q0"}
            stackPush={"00Z"}
          />
          <TransitionFunctionTemplateForm
            ruleNumber={1}
            currentState={"q0"}
            inputSymbol={"0"}
            stackTop={"0"}
            nextState={"q0"}
            stackPush={"000"}
          />
          <TransitionFunctionTemplateForm
            ruleNumber={2}
            currentState={"q0"}
            inputSymbol={"1"}
            stackTop={"0"}
            nextState={"q1"}
            stackPush={"e"}
          />
          <TransitionFunctionTemplateForm
            ruleNumber={3}
            currentState={"q1"}
            inputSymbol={"1"}
            stackTop={"0"}
            nextState={"q1"}
            stackPush={"e"}
          />
          <TransitionFunctionTemplateForm
            ruleNumber={4}
            currentState={"q1"}
            inputSymbol={"e"}
            stackTop={"Z"}
            nextState={"q2"}
            stackPush={"Z"}
          />
        </Form.Group>
        <Button type="submit">Test String</Button>
      </Form>
      <iframe id="hiddenframe" name="hiddenframe"></iframe>
    </>
  );
};

export default Template1Form;

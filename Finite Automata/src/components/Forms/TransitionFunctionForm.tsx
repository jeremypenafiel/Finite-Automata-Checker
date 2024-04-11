import { useState } from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

interface TransitionFunctionFormProps {
  stateCount: number;
}

const TransitionFunctionForm: React.FC<TransitionFunctionFormProps> = ({
  stateCount,
}) => {
  const [ruleCounter, setRuleCounter] = useState(1);

  const handleAddRuleClick = () => {
    setRuleCounter(ruleCounter + 1);
    console.log(ruleCounter);
  };
  const handleDeleteRuleClick = () => {
    if (ruleCounter === 0) {
      return;
    }
    setRuleCounter(ruleCounter - 1);
    console.log(ruleCounter);
  };
  return (
    <Form.Group>
      <button type="button" onClick={handleAddRuleClick}>
        Add Rule
      </button>
      <button type="button" onClick={handleDeleteRuleClick}>
        Delete Rule
      </button>
      {Array.from(Array(ruleCounter)).map((_c, index) => {
        return (
          <InputGroup key={index}>
            <InputGroup.Text>Rule {index + 1}: </InputGroup.Text>
            {/* <Form.Control
              required
              placeholder="Current State"
              name={`CurrentState ${index}`}
            /> */}
            <Form.Select required name={`CurrentState ${index}`}>
              {Array.from(Array(stateCount)).map((_c, index) => {
                return <option key={index}>q{index}</option>;
              })}
            </Form.Select>
            <Form.Control
              required
              placeholder="Input symbol"
              name={`InputSymbol ${index}`}
            />
            <Form.Control
              required
              placeholder="Stack Top"
              name={`StackTop ${index}`}
            />
            <Form.Select required name={`NextState ${index}`}>
              {Array.from(Array(stateCount)).map((_c, index) => {
                return <option key={index}>q{index}</option>;
              })}
            </Form.Select>
            <Form.Control
              required
              placeholder="stack push"
              name={`StackPush ${index}`}
            />
          </InputGroup>
        );
      })}
    </Form.Group>
  );
};

export default TransitionFunctionForm;

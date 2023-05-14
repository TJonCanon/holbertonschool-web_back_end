/* eslint-disable no-unused-vars */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task2 = false;
    const task = true;
  }

  return [task, task2];
}

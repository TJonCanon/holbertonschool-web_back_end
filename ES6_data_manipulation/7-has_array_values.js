export default function hasValuesFromArray(set, array) {
  return array.every((it) => set.has(it));
}

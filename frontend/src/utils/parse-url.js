
const parseUrl = (search) => {
  const paramPart = search.split('?');
  if(paramPart[1]){
    const result = paramPart[1].split('&');
    return result.reduce(function(res, item) {
    if (item) {
      let parts = item.split('=');
      res[parts[0]] = parts[1] || ''
    }
    return res
  }, {})
  }
  return {}

};

export default parseUrl
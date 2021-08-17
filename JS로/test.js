let str = "asdb advg$ af333 fasdf #@#%%@#$";

console.log(str.replace(/[0-9]/g, "[]"));
console.log(str.replace(/[a-zA-Z]/g, "="));
console.log(str.replace(/[!@#$%]/g, "9"));

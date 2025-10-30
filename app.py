import express from "express";
import fetch from "node-fetch";

const app = express();

app.get("/", async (req, res) => {
  const url = "https://raw.githubusercontent.com/SkibidiHub111/Ghoul/refs/heads/main/Ghoul";
  const response = await fetch(url);
  const lua_code = response.ok ? await response.text() : "Error: Không thể tải file Lua từ URL";
  res.type("text/plain").send(lua_code);
});

app.listen(3000, () => console.log("Server running"));

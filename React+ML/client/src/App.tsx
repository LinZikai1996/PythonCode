import { createTheme } from "@mui/material/styles"
import { useMemo } from "react"
import {BrowserRouter, Routes, Route} from "react-router-dom"
import { themeSettings } from "./theme"
import { Box, CssBaseline, ThemeProvider } from "@mui/material"
import Narver from "@/scenes/navbar"
import Dashboard from "@/scenes/dashboard"

function App() {

  const theme = useMemo(() => createTheme(themeSettings), []);

  return (
    <div className='app'>
      <BrowserRouter>
        <ThemeProvider theme={theme}>
          <CssBaseline/>
            <Box width="100%" height="100%" padding="1rem 2rem 4rem">
              <Narver />
              <Routes>
                <Route path='/' element={<Dashboard />}></Route>
                <Route path='/predicitons' element={<div>predictions page</div>}></Route>
              </Routes>
            </Box>
        </ThemeProvider>
      </BrowserRouter>
    </div>
  )
}

export default App

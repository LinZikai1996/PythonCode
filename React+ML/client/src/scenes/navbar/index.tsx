import {useState} from 'react'
import { Link } from 'react-router-dom'
import { Box, Typography, useTheme } from '@mui/material'
import FlewBetween from '@/scenes/navbar/components/FlexBetween'
import AcUnitIcon from '@mui/icons-material/AcUnit';

type Props = {}

const Narver = (props: Props) => {

    const {palette} = useTheme();

    const [selected, setSelected] = useState("dashboard");

    return(
    // 参考笔记 4.1
    <FlewBetween mb="0.25rem" p="0.5 rem 0rem" color={palette.grey[300]}>
        <FlewBetween gap="0.75rem">
            {/* Left side */}
            <AcUnitIcon sx={{fontSize: "28px"}}/>
            <Typography variant='h4' fontSize="16px">
                Finanseer
            </Typography>
        </FlewBetween>
        <FlewBetween gap="2rem">
            <Box sx={{ "&:hover": { color: palette.grey[100] } }}>
                <Link
                    to="/"
                    onClick={() => setSelected("dashboard")}
                    style={{
                    color: selected === "dashboard" ? "inherit" : palette.grey[700],
                    textDecoration: "inherit",
                    }}
                >
                    dashboard
                </Link>
            </Box>
            
            <Box sx={{ "&:hover": { color: palette.grey[100] } }}>
                <Link
                    to="/predictions"
                    onClick={() => setSelected("predictions")}
                    style={{
                    color: selected === "predictions" ? "inherit" : palette.grey[700],
                    textDecoration: "inherit",
                    }}
                >
                    predictions
                </Link>
            </Box>
        </FlewBetween>
    </FlewBetween>
    );
}

export default Narver
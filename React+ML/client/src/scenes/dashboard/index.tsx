import { Box, useMediaQuery, useTheme } from '@mui/material'
import { getGridTemplateLargeScreens, getGridTemplateSmallScreens} from './components/util';
import Row from './components/row';

const Dashboard = () => {

    const {palette} = useTheme();

    const gridTemplateLargeScreens = getGridTemplateLargeScreens();
    const gridTemplateSmallScreens = getGridTemplateSmallScreens();

    const isAboveMediumScreens = useMediaQuery("(min-width: 900px)")

    return (
        // 参考笔记 4.2
        <Box width={"100%"} height={"100%"} display={"grid"} gap={"1.5rem"}            
            sx={
                isAboveMediumScreens
                ? {
                    gridTemplateColumns: "repeat(3, minmax(370px, 1fr))",
                    gridTemplateRows: "repeat(10, minmax(60px, 1fr))",
                    gridTemplateAreas: gridTemplateLargeScreens,
                  }
                : {
                    gridAutoColumns: "1fr",
                    gridAutoRows: "80px",
                    gridTemplateAreas: gridTemplateSmallScreens,
                  }
            }
        >
            <Row data={['a', 'b', 'c']} />
            <Row data={['d', 'e', 'f']} />
            <Row data={['g', 'h', 'i', 'j']} />
        </Box>
    )
}

export default Dashboard
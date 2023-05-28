import DashboardBox from "@/scenes/dashboard/components/dashboardBox";

type Props = {
    data: string[];
}

const Row = (props: Props) => {
  return (
    <>
      {props.data.map((item, index) => (
        <DashboardBox key={index} gridArea={item}></DashboardBox>
      ))}
    </>
  )
}

export default Row
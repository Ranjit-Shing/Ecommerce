import HeroSection from "./components/HeroSection";
import { useProductContext } from "./context/productcontex";

const About = () => {
    const { myName } = useProductContext();

    const data = {
        name: "Ecommerce Zone",
    };

    return (
        <>
            {myName}
            <HeroSection myData={data} />
        </>
    );
};

export default About;
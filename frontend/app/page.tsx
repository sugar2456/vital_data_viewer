"use client";
import { lusitana  } from './ui/fonts';
export default function Home() {
  return (
    <p className={`${lusitana.className} text-xl text-gray-800 md:text-3xl md:leading-normal`}>
      Hello, world!
    </p>
  );
}

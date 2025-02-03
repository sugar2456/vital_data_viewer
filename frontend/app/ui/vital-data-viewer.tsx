import { GlobeAltIcon } from '@heroicons/react/24/outline';
import { lusitana } from '@/app/ui/fonts';

export default function VitalDataLogo() {
  return (
    <div
      className={`${lusitana.className} flex flex-col items-center leading-none text-white`}
    >
      <p className="text-[32px]">Vital Data</p>
      <p className="text-[32px]">Viewer</p>
    </div>
  );
}
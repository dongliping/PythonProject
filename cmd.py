import  argparse

parser=argparse.ArgumentParser(description="hahaha  this is command")
parser.add_argument("--ParaA",help="I am A",type=int)
parser.add_argument("--ParaB",help="I am B",type=int)
args=parser.parse_args()
if args.ParaA:
    print("it is a {}".format(args.ParaA))
if args.ParaB:
    print("it is b {}".format(args.ParaB))
if args.ParaA and args.ParaB:
    print("It's aa is {},it's ba is {}".format(args.ParaA,args.ParaB))
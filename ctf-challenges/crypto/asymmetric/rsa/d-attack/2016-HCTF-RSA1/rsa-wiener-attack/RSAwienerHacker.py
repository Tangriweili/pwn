'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic
import gmpy2
import binascii
from Crypto.Util.number import long_to_bytes


def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        #check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s * s - 4 * n
            if (discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d


# TEST functions


def solve(n, e):
    print("Testing Wiener Attack")
    times = 5
    while (times > 0):
        hacked_d = hack_RSA(e, n)
        print("hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1


if __name__ == "__main__":
    bt = 536380958350616057242691418634880594502192106332317228051967064327642091297687630174183636288378234177476435270519631690543765125295554448698898712393467267006465045949611180821007306678935181142803069337672948471202242891010188677287454504933695082327796243976863378333980923047411230913909715527759877351702062345876337256220760223926254773346698839492268265110546383782370744599490250832085044856878026833181982756791595730336514399767134613980006467147592898197961789187070786602534602178082726728869941829230655559180178594489856595304902790182697751195581218334712892008282605180395912026326384913562290014629187579128041030500771670510157597682826798117937852656884106597180126028398398087318119586692935386069677459788971114075941533740462978961436933215446347246886948166247617422293043364968298176007659058279518552847235689217185712791081965260495815179909242072310545078116020998113413517429654328367707069941427368374644442366092232916196726067387582032505389946398237261580350780769275427857010543262176468343294217258086275244086292475394366278211528621216522312552812343261375050388129743012932727654986046774759567950981007877856194574274373776538888953502272879816420369255752871177234736347325263320696917012616273L
    e = 0x10194521505692a64d043daaef7647e0efb1503ec89220a0e4148ab53ecf708146a8893a2e700e4f2f062be14a3ab4e46339a939d5c7289904cc0ab043320d3a4d7da868bf5736ae5f787d6c0e3d9b8cc4b81314ad6c5ff643bc0d8946fea7eb09bf707a54747a39df1cfc0c30849770578cb63de86621001ce86a11874c91419a4d07373e66e94f31b988cac3aeaff88c7abaf3b78468a434990f7854e734208a7461f8245660fa8301f979e85517d705302c797dbdf2938cc442b01c228939eb73aa29651a198a332af2bb982310699684e5a0595c7413ec01eefb3613a9ea4b59f1de984ad4bf6654960613c0f8104b4e41fb33384e07f715176d68f4bb7613b1258675e70dc774f701aee053830f0be28ba9f308c9fe1707a5ba07a2027d74144b8aeb4042df3c1d73d9c38c2d7d1a890fd70d6e38c72da5d075f3811c0354dcecdd836a59112a70be22757278c5e4973906aaeeadd6f61d0845d6f9761df191b0b2527d122dd07f8bd07f5cd14268246ac2b93b778c84b5157f7eb23a8eaa9f0f885f2a38e3fb8fd1012d9b6c841cea8d9d73b232bef298afd086c1063bdd11e0777c8d2ec91ae843a67a98039cb53fad0ee25040176841a017fabf79b98de21d40bc6985f82dd84406aad26e9ac9bc5f6e12385230d9620b888c201ca9c413cbf0f36b100a6c62c5c8f065934fcf9f9f0179eea35888cb357b704441c1
    t = gmpy2.invert(e, bt)
    print hex(t)
    n = 0x4b4403cd5ac8bdfaa3bbf83decdc97db1fbc7615fd52f67a8acf7588945cd8c3627211ffd3964d979cb1ab3850348a453153710337c6fe3baa15d986c87fca1c97c6d270335b8a7ecae81ae0ebde48aa957e7102ce3e679423f29775eef5935006e8bc4098a52a168e07b75e431a796e3dcd29c98dab6971d3eac5b5b19fb4d2b32f8702ef97d92da547da2e22387f7555531af4327392ef9c82227c5a2479623dde06b525969e9480a39015a3ed57828162ca67e6d41fb7e79e1b25e56f1cff487c1d0e0363dc105512d75c83ad0085b75ede688611d489c1c2ea003c3b2f81722cdb307a3647f2da01fb3ba0918cc1ab88c67e1b6467775fa412de7be0b44f2e19036471b618db1415f6b656701f692c5e841d2f58da7fd2bc33e7c3c55fcb8fd980c9e459a6df44b0ef70b4b1d813a57530446aa054cbfb9d1a86ffb6074b6b7398a83b5f0543b910dcb9f111096b07a98830a3ce6da47cd36b7c1ac1b2104ea60dc198c34f1c50faa5b697f2f195afe8af5d455e8ac7ca6eda669a5a1e3bfbd290a4480376abd1ff21298d529b26a4e614ab24c776a10f5f5d8e8809467a3e81f04cf5d5b23eb4a3412886797cab4b3c5724c077354b2d11d19ae4e301cd2ca743e56456d2a785b650c7e1a727b1bd881ee85c8d109792393cc1a92a66b0bc23b164146548f4e184b10c80ec458b776df10405b65399e32d657bc83e1451
    p = 0x94121F49C0E7A37A60FDE4D13F021675ED91032EB16CB070975A3EECECE8697ED161A27D86BCBC4F45AA6CDC128EB878802E0AD3B95B2961138C8CD04D28471B558CD816279BDCCF8FA1513A444AF364D8FDA8176A4E459B1B939EBEC6BB164F06CDDE9C203C612541E79E8B6C266436AB903209F5C63C8F0DA192F129F0272090CBE1A37E2615EF7DFBB05D8D88B9C964D5A42A7E0D6D0FF344303C4364C894AB7D912065ABC30815A3B8E0232D1B3D7F6B80ED7FE4B71C3477E4D6C2C78D733CF23C694C535DB172D2968483E63CC031DFC5B27792E2235C625EC0CFDE33FD3E53915357772975D264D24A7F31308D72E1BD7656B1C16F58372E7682660381
    q = 0x8220863F1CFDA6EDE52C56B4036485DB53F57A4629F5727EDC4C5637603FE059EB44751FC49EC846C0B8B50966678DFFB1CFEB350EC44B57586A81D35E4887F1722367CE99116092463079A63E3F29D4F4BC416E7728B26248EE8CD2EFEA6925EC6F455DF966CEE13C808BC15CA2A6AAC7FEA69DB7C9EB9786B50EBD437D38B73D44F3687AEB5DF03B6F425CF3171B098AAC6708D534F4D3A9B3D43BAF70316812EF95FC7EBB7E224A7016D7692B52CB0958951BAB4FB5CB1ABB4DAC606F03FA15697CC3E9DF26DE5F6D6EC45A683CD5AAFD58D416969695067795A2CF7899F61669BC7543151AB700A593BF5A1E5C2AFBCE45A08A2A9CC1685FAF1F96B138D1
    if p * q == n:
        print 'true'
    phin = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phin)
    cipher = 0x2517d1866acc5b7b802a51d6251673262e9e6b2d0e0e14a87b838c2751dee91e4ea29019b0a7877b849fddf9e08580d810622db538462b529412eba9d0f8a450fe1889021c0bbd12a62ccc3fff4627b1dbdebec3a356a066adc03f7650722a34fe41ea0a247cb480a12286fffc799d66b6631a220b8401f5f50daa12943856b35e59abf8457b2269efea14f1535fb95e56398fd5f3ac153e3ea1afd7b0bb5f02832883da46343404eb44594d04bbd254a9a35749af84eaf4e35ba1c5571d41cab4d58befa79b6745d8ecf93b64dd26056a6d1e82430afbff3dbc08d6c974364b57b30c8a8230c99f0ec3168ac4813c4205d9190481282ae14f7b94400caff3786ed35863b66fefcffbef1ad1652221746a5c8da083987b2b69689cf43e86a05ce4cf059934716c455a6410560e41149fbcf5fcea3c210120f106b8f6269b9a954139350626cf4dcb497ce86264e05565ec6c6581bf28c643bb4fab8677148c8034833cedacb32172b0ff21f363ca07de0fa2882ac896954251277adc0cdd0c3bd5a3f107dbebf5f4d884e43fe9b118bdd51dc80607608670507388ae129a71e0005826c7c82efccf9c86c96777d7d3b9b5cce425e3dcf9aec0643f003c851353e36809b9202ff3b79e8f33d40967c1d36f5d585ac9eba73611152fc6d3cf36fd9a60b4c621858ed1f6d4db86054c27828e22357fa3d7c71559d175ff8e8987df
    flag = gmpy2.powmod(cipher, d, n)
    print long_to_bytes(flag)
    #solve(n, t)
